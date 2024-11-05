from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, EditForm, DeleteForm
import json
import os

userfile_name = "app/user.json"

@app.route('/')
@app.route('/index')
def index():    
    # if file is empty the return an empty list
    users = []
    if os.path.exists(userfile_name):
        users_file = open(userfile_name, 'r')
        users = json.load(users_file)
    
    return render_template('index.html', title='Home', users=users)

@app.route('/login', methods=['GET', 'POST'])

def login():
    form = LoginForm()
    if form.validate_on_submit():
        users = []
        if os.path.exists(userfile_name):
            userfile = open(userfile_name, 'r')
            users = json.load(userfile)
            userfile.close()
        new_entry = {'username': form.username.data, 'password': form.password.data}
        users = users + [new_entry]
        print(users)
        userfile = open(userfile_name, 'w')
        json.dump(users, userfile)
        userfile.close()
        return redirect(url_for('index'))
    
@app.route('/edit', methods=['GET', 'POST'])

def edit():
    form = EditForm()
    if form.validate_on_submit():
        users = []
        if os.path.exists(userfile_name):
            userfile = open(userfile_name, 'r')
            users = json.load(userfile)
            userfile.close()
        entry_to_edit = {'username': form.username.data, 'password': form.currentpassword.data}
        newpassword = form.newpassword.data
        # find the entry to edit and if current password matches then update the password
        for entry in users:
            if entry['username'] == entry_to_edit['username'] and entry['password'] == entry_to_edit['password']:
                entry['password'] = newpassword
        
        print(users)
        userfile = open(userfile_name, 'w')
        json.dump(users, userfile)
        userfile.close()
        return redirect(url_for('index'))


    return render_template('edit.html', title='Edit Password', form=form)

@app.route('/delete', methods=['GET', 'POST'])

def delete():
    form = DeleteForm()
    if form.validate_on_submit():
        users = []
        if os.path.exists(userfile_name):
            userfile = open(userfile_name, 'r')
            users = json.load(userfile)
            userfile.close()
        entry_to_delete = {'username': form.username.data, 'password': form.password.data}
        # find the entry to delete and if current password matches then delete the entry
        for entry in users:
            if entry['username'] == entry_to_delete['username'] and entry['password'] == entry_to_delete['password']:
                users.remove(entry)
        
        print(users)
        userfile = open(userfile_name, 'w')
        json.dump(users, userfile)
        userfile.close()
        return redirect(url_for('index'))

    return render_template('delete.html', title='Delete User', form=form)