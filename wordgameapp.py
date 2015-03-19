from flask import Flask, render_template, url_for, request, redirect, flash, session
from time import time, gmtime, strftime
from random import randint

app = Flask(__name__)
start_time = 0

def getTime():
	return time()

def update_log(user, time):
	users = open("users.txt", 'r')
	lines = []
	lines.append(time + ': ' + user + '\n')
	for line in users.readlines():
		lines.append(line)
	lines.sort()
	with open("users.txt", 'w') as usr:
		for line in lines:
			usr.write(''.join(line))

@app.route('/displayranked')
def showranks():
	with open('users.txt') as ranks:
		lines = ranks.readlines()
		lines = lines[:10]
		return render_template('show.html', the_title="Here are the top ranked players to date", the_ranked=lines, home_link=url_for("display_index"))

def get_line_number(user):
	with open('users.txt') as f:
		for i, line in enumerate(f, 1):
			if user in line:
				return i

@app.route('/')
def display_index():
	with open("sourcewords.txt", 'r') as source_words:
		words = source_words.readlines()
		number = randint(0, len(words))
		session['source_word'] = words[number]
	session['start_time'] = getTime()
	return render_template("index.html", the_title="The Word Game", base_word=session['source_word'], the_save_url=url_for("populateAttempts"), ranked_url=url_for("showranks"))

@app.route('/savename', methods=['POST'])
def log_name_time():
	if request.form['player_name'] == "":
		name = "shy person".title()
	else:
		name = request.form['player_name'].title()
	update_log(name, session['total_time'])
	placement = get_line_number(session['total_time'] + ': ' + name)
	return render_template("rank.html", the_title="Well done!", rank=placement, time_took=session['total_time'], home_link=url_for("display_index"), ranked_url=url_for("showranks"))

@app.route('/saveform', methods=['POST'])
def populateAttempts():
	all_ok = True
	for i in range(0,7):
		if (request.form ['user_guess_' + str(i+1)] == ''):
			all_ok = False
	if not all_ok:
		flash("sorry you must fill in all boxes, Try again!")
	if all_ok:
		end_time = getTime()
		session['total_time'] = gmtime(end_time - session['start_time'])
		session['total_time'] = strftime("%M:%S",session['total_time'])
		attempts = []
		for i in range(0,7):
			attempts.append(request.form['user_guess_' + str(i+1)])
		good_words = []
		bad_words = []
		for attempt in attempts:
			attempt = attempt.lower()
			bad = False
			duplicate = False
			for good in good_words:
				if attempt == good:
					bad_words.append(attempt + " : This word was duplicated!")
					duplicate = True
			if duplicate:
				pass
			elif len(attempt) < 3:
				bad_words.append(attempt + " : This word was too short!")
			elif attempt == ''.join(session['source_word']):
				bad_words.append(attempt + " : This word was the same as the source word!")
			else:
				word = list(attempt)
				for i in word:
					if word.count(i) > session['source_word'].count(i):
						bad = True
						break
				if bad:
					bad_words.append(''.join(word) + " : This word had letters that the source word did not have!")
				else:
					good_words.append(attempt)
		for item in good_words:
			if item in open('validwords.txt').read():
				pass
			else:
				bad_words.append(''.join(item) + " : This word was not in the valid words list!")
		if len(bad_words) > 0:
			message = "Sorry, you got the following words wrong! "
		else:
			message = "Well done, you got all the words right!"
		return render_template("thanks.html", the_title="Thanks", incorrect_words=bad_words, home_link=url_for("display_index"), time_took=session['total_time'], msg=message, user_name_url=url_for("log_name_time"))
	else:
		return redirect(url_for("display_index"))

app.config['SECRET_KEY'] = 'thisismysecretkeywhichyouwillneverguesshahahahahahahahaha'

if __name__ == "__main__":
	app.run()

