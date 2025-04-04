import sqlite3
from flask import Flask,render_template,request,redirect

app = Flask(__name__,static_url_path='/static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    conn=sqlite3.connect('database.db')
    c=conn.cursor()
    c.execute('SELECT id, question, option1, option2, option3, option4 FROM questions')
    questions=[
        (1,"What is the keyword used to define a function in Python?", "func", "define", "def", "function"),
        (2,"Which data type is used to store multiple items in a single variable?", "int", "list", "str", "bool"),
        (3,"Which symbol is used for single-line comments in Python?", "//", "#", "/*", "--"),
        (4,"Which function is used to display output in Python?", "print()", "echo()", "display()", "show()"),
        (5,"Which operator is used for exponentiation in Python?", "^", "**", "*", "//")
    ]
    conn.close()
    return render_template('quiz.html',questions=questions,request=request)
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute('SELECT id, question, correct_answer FROM questions')
        questions = c.fetchall() 

        conn.close()
        score = 0
        total_questions = len(questions)
        user_answers = {}
        correct_answers = {}

        for q in questions:
            if len(q) == 3:  
                q_id, question_text, correct_answer = q
                user_answer = request.form.get(f'q{q_id}')
                user_answers[q_id] = user_answer if user_answer else "Not Answered"
                correct_answers[q_id] = correct_answer

                if user_answer == correct_answer:
                    score += 1
                           
        return render_template('result.html', score=score, total=total_questions, 
                               user_answers=user_answers, correct_answers=correct_answers, questions=questions,request=request)

if __name__ == '__main__':
    app.run(debug=True) 