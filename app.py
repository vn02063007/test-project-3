from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd

app = Flask(__name__, template_folder='templates')

def get_data():
    engine = create_engine('sqlite:///database.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    query = '''SELECT "Condition Point", COUNT(*) as Count
    FROM database
    GROUP BY "Condition Point"'''
    # fetch the data using pandas
    data = pd.read_sql_query(query, engine)
    return data.to_dict(orient='records')

@app.route('/')
def index():
    data = get_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
