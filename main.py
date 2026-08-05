from analysis.text_analysis import analyze_file
from utils.logger import write_log

def menu():
    while True:
        print("\n" + "=" * 40)
        print("        CryptoLabX Toolkit")
        print("=" * 40)
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Attack")
        print("4. Analyze Text File")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            write_log("Encrypt")
            print("\nEncrypt Module - Coming Soon!")

        elif choice == "2":
            write_log("Decrypt")
            print("\nDecrypt Module - Coming Soon!")

        elif choice == "3":
            write_log("Attack")
            print("\nAttack Module - Coming Soon!")

        elif choice == "4":
            write_log("Analyze text file")
            filename = input("\nEnter file path: ")
            analyze_file(filename)

        elif choice == "5":
            write_log("Exit")
            print("\nThank you for using CryptoLab1!")
            break

        else:
            print("\nInvalid Choice! Try Again.")


if __name__ == "__main__":
    menu()