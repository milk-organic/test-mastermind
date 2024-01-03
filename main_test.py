from pyscript import document
import numpy as np

candidate_history = []

def generate_all_possible_codes(length, current_code=[]):
    """指定された長さのすべての可能なコードのリストを再帰的に生成する関数"""
    if length == 0:
        return [tuple(current_code)]
    
    all_codes = []
    for digit in range(4):
        all_codes.extend(generate_all_possible_codes(length - 1, current_code + [digit]))
    
    return all_codes

def evaluate_guess(secret_code, guess):
    """ヒントを生成する関数。正しい数字と位置の数、正しい数字だが位置が異なる数を返す"""
    correct_position = sum(s == g for s, g in zip(secret_code, guess))
    correct_number = sum(min(secret_code.count(digit), guess.count(digit)) for digit in set(secret_code)) - correct_position
    return correct_position, correct_number

def mastermind_solver(candidate_history, candidates, code, correct_position, correct_number):
    """Mastermindのソルバー関数"""
    if correct_position == code_length:
        print(f"CPUの推測が正解です！正解コード: {code}")

    matching_codes = [c for c in candidates if evaluate_guess(list(map(int, code)), c) == (correct_position, correct_number)]
    candidate_history.append(matching_codes)

    if not matching_codes:
        current_guess = None
        print("エラー: 与えられたヒントに一致するコードが見つかりませんでした。")
    else:
        current_guess = matching_codes[np.random.randint(len(matching_codes))]
        # print(f"CPUの推測: {current_guess}")
    
    return candidate_history, matching_codes, current_guess

def translate_english():
    newData = {
        "data": 0,
        "guess": "R, L, U, D",
        "correctPlace": 2,
        "wrongPlace": 1, 
        "all_possible_codes": None, 
    }

    tbody = document.querySelector("#old-guesses")

    newRow = document.createElement("tr")

    newRow.innerHTML = "<td" + newData.data + "</td>" + "<td>" + newData.guess + "</td>" +\
        "<td>" + newData.correctPlace + "</td>" +\
        "<td>" + newData.wrongPlace + "</td>" +\
        '<td><button class="btn btn-primary" py-click="edit_guess">edit</button></td>'

    tbody.appendChild(newRow)

if __name__ == "__main__":
    code_length = 4
    all_possible_codes = generate_all_possible_codes(code_length)
    code = (0, 1, 2, 3)
    correct_position, correct_number = 1, 1
    candidate_history, all_possible_codes, current_guess = mastermind_solver(candidate_history, all_possible_codes, code, correct_position, correct_number)
    

