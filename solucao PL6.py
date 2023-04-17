from flask import Flask, request, make_response, jsonify
import sqlite3

app = Flask(__name__)

# database initialization
conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS alunos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, idade INTEGER)')
c.execute('CREATE TABLE IF NOT EXISTS notas (id INTEGER PRIMARY KEY AUTOINCREMENT, aluno_id INTEGER, ano TEXT, cadeira TEXT, nota INTEGER)')
conn.commit()

@app.route('/aluno', methods=['PUT'])
@app.route('/aluno/<int:id>', methods=['GET'])
def aluno(id=None):
    if request.method == 'GET':
        # search for student with given id
        c.execute("SELECT nome, idade FROM alunos WHERE id = ?", (id,))
        student = c.fetchone()
        if not student:
            return make_response(jsonify({'error': 'Student not found'}), 404)
        data = {'id': id, 'nome': student[0], 'idade': student[1]}
        return make_response(jsonify(data), 200)
    elif request.method == 'PUT':
        # insert new student into database
        data = request.get_json()
        nome = data['nome']
        idade = data['idade']
        c.execute("INSERT INTO alunos (nome, idade) VALUES (?, ?)", (nome, idade))
        new_id = c.lastrowid
        conn.commit()
        response_data = {'id': new_id}
        response_headers = {'Location': f'/aluno/{new_id}'}
        return make_response(jsonify(response_data), 201, response_headers)

@app.route('/notas', methods=['POST', 'GET'])
def notas():
    if request.method == 'POST':
        # insert new grade into database
        data = request.get_json()
        aluno_id = data['aluno_id']
        ano = data['ano']
        cadeira = data['cadeira']
        nota = data['nota']
        c.execute("INSERT INTO notas (aluno_id, ano, cadeira, nota) VALUES (?, ?, ?, ?)", (aluno_id, ano, cadeira, nota))
        conn.commit()
        response_data = {'message': 'Grade inserted successfully'}
        return make_response(jsonify(response_data), 201)
    elif request.method == 'GET':
        # search for grades with given query parameters
        ano = request.args.get('ano')
        cadeira = request.args.get('cadeira')
        c.execute("SELECT alunos.nome, notas.ano, notas.cadeira, notas.nota FROM notas INNER JOIN alunos ON alunos.id = notas.aluno_id WHERE notas.ano = ? AND notas.cadeira = ?", (ano, cadeira))
        results = c.fetchall()
        data = [{'nome': result[0], 'ano': result[1], 'cadeira': result[2], 'nota': result[3]} for result in results]
        return make_response(jsonify(data), 200)

if __name__ == '__main__':
    app.run(debug=True)
