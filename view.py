import text
import uuid

def print_msg(msg:str):
	print('\n' + '=' *len(msg))
	print(msg)
	print('=' *len(msg)+'\n')


def show_menu(menu: list[str])-> int:
	flag = True
	for i, item in enumerate(menu):
		if i!=0:
			print(f'\t{i}. {item}')
		else:
			print(item)
	input_select = input("Выберите пункт меню: ")
	while flag:
		if input_select.isdigit() and 0 < int(input_select) < len(menu):
			flag = False
			return int(input_select)
		else:
			print(text.menu_error)
			input_select = input("Выберите пункт меню: ")

def show_notes(data: list[dict[str,list[dict[str,str]]]], msg: str):
	if data:
		lists = sorted(data, key=lambda k: list(k)[0])
		print('\n' + '='*100 + '\n')
		for i in lists:
			for key, value in i.items():
				date = key
				uid = value[0].get('id')
				title = value[1].get('title')
				body = value[2].get('body')
				print(f"date - {date}, id - {uid}, title - {title}, body - {body}\n")
		print('=' * 100+'\n')
	else:
		print_msg(text.empty_notes)

def add_note(input_fields: list[str])->list[dict[str,str]]:
	new_note = []
	for i in range(1):
		new_note.append({'id':str(uuid.uuid4())})
		title = input(input_fields[0])
		body = input(input_fields[1])
		new_note.append({'title':title})
		new_note.append({'body':body})
	return new_note

def ask_find(msg: str)->str:
	return input(msg)

def ask_change(input_fields: list[str]) -> list[str]:
    new_note = []
    for item in input_fields:
        new_note.append(input(item))
    return new_note