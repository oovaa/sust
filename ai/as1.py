class ITSupportAgent:
    def __init__(self) -> None:
        self.greetings = (
            "Hello there, I'm an agent created by Omar designed to help you troubleshoot and fix problems.\n"
            "So tell me, what problem do you have?"
        )
        self.apology = (
            "I'm sorry, but I don't have a solution for that problem at the moment."
        )

        self.prob_slo = {
            "no internet access": [
                "Check cables",
                "Report to the internet connection provider",
                "Check your network configuration",
            ],
            "forgot user password": [
                "Reset the password through email",
                "Use password recovery option",
                "Contact the system administrator",
            ],
            "software not working": [
                "Restart the software",
                "Update the software to the latest version",
                "Check for any error messages",
            ],
            "computer running slow": [
                "Close unnecessary programs",
                "Clear temporary files",
                "Upgrade hardware components",
            ],
        }

    def list_solutions(self, solutions):
        print("Here are some fixes you should consider:")
        for num, sol in enumerate(solutions, 1):
            print(f"{num}. {sol}")
        print("You can contact me again if anything.")

    def run(self):
        print(self.greetings)
        question = input()

        if question not in self.prob_slo:
            print(self.apology)
            return

        solutions_list = self.prob_slo[question]
        self.list_solutions(solutions_list)


if __name__ == "__main__":
    agent = ITSupportAgent()
    agent.run()
