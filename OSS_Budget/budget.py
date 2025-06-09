import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

    def edit(self): # 기능 추가 1 (수정하기)
        if not self.expenses:
            print("수정할 지출 내역이 없습니다.\n")
            return

        self.list_expenses()

        try:
            expense_index = int(input("수정할 지출 번호를 입력하세요: ")) - 1
            if not (0 <= expense_index < len(self.expenses)):
                print("유효하지 않은 지출 번호입니다.\n")
                return
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.\n")
            return
        expense_to_edit = self.expenses[expense_index]
        print(f"\n현재 지출: {expense_to_edit}")
        print("새로운 정보를 입력하세요 (변경하지 않으려면 Enter):")

        # 카테고리 수정
        new_category = input(f"새 카테고리 (현재: {expense_to_edit.category}): ")
        if new_category: # 입력이 있으면 업데이트
            expense_to_edit.category = new_category

        # 설명 수정
        new_description = input(f"새 설명 (현재: {expense_to_edit.description}): ")
        if new_description: # 입력이 있으면 업데이트
            expense_to_edit.description = new_description

        # 금액 수정
        while True:
            new_amount_str = input(f"새 금액(원) (현재: {expense_to_edit.amount}): ")
            if not new_amount_str: # 입력이 없으면 현재 금액 유지
                break
            try:
                new_amount = int(new_amount_str)
                if new_amount <= 0:
                    print("금액은 0보다 커야 합니다.")
                    continue
                expense_to_edit.amount = new_amount
                break
            except ValueError:
                print("잘못된 금액입니다. 숫자를 입력해주세요.")
        
        # 날짜는 수정하지 않도록 함 (날짜 수정 기능도 필요하다면 추가 가능)
        # expense_to_edit.date = datetime.date.today().isoformat() # 오늘 날짜로 업데이트 하고 싶다면 이 코드 사용

        print("지출 내역이 성공적으로 수정되었습니다.\n")

    def delete(self):  #기능 추가 2 (삭제하기)
        if not self.expenses:
            print("삭제할 지출 내역이 없습니다.\n")
            return

        self.list_expenses()

        try:
            expense_index = int(input("삭제할 지출 번호를 입력하세요: ")) - 1
            if not (0 <= expense_index < len(self.expenses)):
                print("유효하지 않은 지출 번호입니다.\n")
                return
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.\n")
            return

        deleted_expense = self.expenses.pop(expense_index) 
        print(f"'{deleted_expense.description}' 지출이 삭제되었습니다.\n")






