import json
import datetime
import os

original_notes = []
your_notes = []
path = 'notes.json'

def open_file():
	original_notes.clear()
	your_notes.clear()
	with open(path, 'r', encoding='UTF-8') as file:
		if (os.stat('notes.json').st_size == 0):
			return
		get_notes = json.load(file)
	for i in get_notes:
		notes = {}
		for key, value in i.items():
			date = key
			uid = value[0].get('id')
			title = value[1].get('title')
			body = value[2].get('body')
		notes[date] = [{'id': uid},{'title': title},{'body':body}]
		your_notes.append(notes)
		original_notes.append(notes)

def add_contact(add:list[dict[str,str]]):
	notes = {}
	dt_now = datetime.datetime.now()
	notes[str(dt_now)]=(add)
	your_notes.append(notes)

def save_file():
	with open(path, 'w', encoding='UTF-8') as file:
		json.dump(your_notes, file)

def search_function(item: str)-> dict[str,list[dict[str,str]]]:
	find = {}
	result = []
	str_for_search = ''
	for i in your_notes:
		str_for_search = ''
		for key, value in i.items():
			str_for_search+=value[1].get('title')
			str_for_search+=value[2].get('body')
			if item in str_for_search:
				date = key
				uid = value[0].get('id')
				title = value[1].get('title')
				body = value[2].get('body')
				find[date] = [{'id': uid},{'title': title},{'body':body}]
	result.append(find)
	return result
	
def change(list_find:list[dict[str,list[dict[str,str]]]], new: str):
	notes = {}
	dt_old = ''
	count=0
	for i in list_find:
		for key in i.keys():
			dt_old = key
	for i in list_find:
		for _, value in i.items():
			dt_now= str(datetime.datetime.now())
			uid = value[0].get('id')
			title = value[1].get('title')
			body = value[2].get('body')
			if new[0] != '':
				title = new[0]
			if new[1] != '':
				body = new[0]
			notes[dt_now] = [{'id': uid},{'title': title},{'body':body}]
	for i in your_notes:
		if(dt_old in i.keys()):
			i.keys() == dt_old
			break
		else:
			count+=1
	your_notes[count] = notes

def delete_text(res:list[dict[str,list[dict[str,str]]]]):
	your_notes.remove(res[0])