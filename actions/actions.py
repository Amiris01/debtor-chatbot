from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionFetchDebtDetails(Action):

    def name(self) -> str:
        return "action_fetch_debt_details"

    def run(self, dispatcher, tracker, domain):
        total_amount = "5000 USD"
        interest_rate = "5.5"
        debt_breakdown = "Principal: 4000 USD, Interest: 1000 USD"

        return [SlotSet("total_amount", total_amount),
                SlotSet("interest_rate", interest_rate),
                SlotSet("debt_breakdown", debt_breakdown)]

class ActionResetTotalAmount(Action):
    def name(self):
        return "action_reset_total_amount"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("total_amount", None)]

class ActionCheckIfSlotFilled(Action):
    def name(self):
        return "action_check_if_slot_filled"

    def run(self, dispatcher, tracker, domain):
        total_amount = tracker.get_slot("total_amount")
        
        if total_amount:
            dispatcher.utter_message(text=f"Your total debt is {total_amount}.")
            return [SlotSet("total_amount", total_amount)]
        else:
            dispatcher.utter_message(text="I will fetch your debt details now.")
            return [SlotSet("total_amount", "5000 USD")]
        
class ActionSetPaymentOption(Action):
    def name(self) -> str:
        return "action_set_payment_option"

    async def run(self, dispatcher, tracker, domain):
        payment_option = tracker.get_intent_of_latest_message()

        if payment_option == "choose_full_payment":
            return [SlotSet("payment_option", "full payment")]
        elif payment_option == "choose_installment_payment":
            return [SlotSet("payment_option", "installment")]
        elif payment_option == "choose_partial_payment":
            return [SlotSet("payment_option", "partial payment")]
        else:
            return [SlotSet("payment_option", None)]