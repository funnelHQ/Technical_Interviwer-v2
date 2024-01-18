
from flask import Blueprint,Flask,render_template, jsonify, request
from app.models import db, Candidate
import csv
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

app_routes = Blueprint('app_routes', __name__)




questions = []
current_question_index = 0
 

with open('python_oops_questions.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        questions.append(row)

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()
def preprocess_text(text):#preprocesses the input text
    tokens = word_tokenize(text.lower())#tokenize
    filtered_tokens = [stemmer.stem(token) for token in tokens if token.isalpha() and token not in stop_words]#stemming filtering
    return filtered_tokens
def check_similarity(candidate_response, expected_answer):#check the similatrity based on method of jacob check
    candidate_tokens = preprocess_text(candidate_response)
    expected_tokens = preprocess_text(expected_answer)

    intersection = len(set(candidate_tokens).intersection(expected_tokens))
    union = len(set(candidate_tokens).union(expected_tokens))
    similarity = intersection / union if union > 0 else 0

    return similarity

@app_routes.route('/index')
def index():
    return render_template('index.html')


@app_routes.route('/ask_question', methods=['GET'])
def ask_question():#Show the question in progress
    global current_question_index
    if current_question_index < len(questions):
        current_question = questions[current_question_index]
        current_question_index += 1
        return jsonify({
            'question_id': current_question_index,
            'question': current_question['question']
        })
    else:
        return jsonify({'message': 'No more questions available'})



@app_routes.route('/test_correctness', methods=['POST'])
def test_correctness():#test the correctness 
    global current_question_index

    candidate_response = request.json['candidate_response']#get by frontend
    candidate_id = request.json['candidate_id']#get by frontend  

    if current_question_index > 0 and current_question_index <= len(questions):#check for the emptying of questions in file
        current_question = questions[current_question_index - 1]
        expected_answer = current_question['answer']
        similarity = check_similarity(candidate_response, expected_answer)

        try:
            candidate = Candidate.query.filter_by(id=candidate_id).first()#if in db 

            if candidate is None:#if not in db
                candidate = Candidate(id=candidate_id, name=f"Candidate {candidate_id}", round_number=1, score=0)
                db.session.add(candidate)#add to db
                db.session.commit()

            
            if similarity >= 0.4:#if similarity score is in rrequired range
                result = "Correct"
                candidate.score += 1  
                db.session.commit() 
            else:
                result = "Incorrect"

            return jsonify({
                'question': current_question['question'],
                'candidate_response': candidate_response,
                'result': result,
                'candidate_id': candidate_id,
                'success': True
            })

        except Exception as e:
            db.session.rollback()  
            return jsonify({'error': str(e), 'success': False})
    else:
        return jsonify({'error': 'Invalid question index', 'success': False})





@app_routes.route('/get_round_scores/<int:round_number>', methods=['GET'])
def get_round_scores(round_number):
    scores = Candidate.query.filter_by(round_number=round_number).order_by(Candidate.score.desc()).all()
    score_data = [{'candidate_id': candidate.id, 'score': candidate.score} for candidate in scores]
    return jsonify({'round_number': round_number, 'scores': score_data})
