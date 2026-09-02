from dataclasses import dataclass

@dataclass
class Account:
    name:str
    balance:float
    gender:str

class AccountReport:
    @staticmethod
    def generate_report(*accounts: Account) -> dict:
        report = {
            "male_account": [],
            "female_account": [],
            "male_sum": 0,
            "female_sum": 0,
        }

        for account in accounts:
            if account.gender.strip().lower() == "male":
                report["male_account"].append(account.name)
                report["male_sum"] += account.balance
            elif account.gender.strip().lower() == "female":
                report["female_account"].append(account.name)
                report["female_sum"] += account.balance

        return report


ram_account = Account("Ram", 100, "Male")
sita_account = Account("Sita", 200, "Female")
shyam_account = Account("Shyam", 300, "Male")
gita_account = Account("Gita", 400, "Female")

report = AccountReport.generate_report(ram_account,sita_account,shyam_account,gita_account)
print(report)

                     
                    