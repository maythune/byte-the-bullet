from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

nutrition_info = {
    "ask_carbohydrates": "Carbohydrates are your body's main energy source, found in grains, fruits, and vegetables.",
    "ask_healthy_carbs": "Healthy carbs include whole grains, legumes, fruits, and vegetables.",
    "ask_unhealthy_carbs": "Unhealthy carbs are refined sugars, pastries, and sugary drinks.",
    "ask_add_healthy_carbs": "Add healthy carbs by choosing whole grains, beans, lentils, fruits, and veggies.",
    "ask_diet": "A healthy diet includes a balance of protein, carbohydrates, fats, vitamins, and minerals.",
    "ask_healthy_eating_plate": "The Healthy Eating Plate emphasizes vegetables, fruits, whole grains, healthy protein, and water.",
    "ask_diabetes": "Diabetes is a condition where blood sugar levels are too high due to insulin issues.",
    "ask_hypoglycemia": "Hypoglycemia is low blood sugar, causing shakiness, sweating, and confusion.",
    "ask_protein": "Proteins are essential for building and repairing tissues, found in meat, fish, eggs, and legumes.",
    "ask_protein_needs": "Protein needs depend on weight and activity level, typically 0.8–1.5g per kg of body weight.",
    "debunk_carbs_myth": "Carbs do not inherently make you fat; excessive calories do. Focus on quality carbs."
}

class ActionMultiNutrition(Action):
    def name(self) -> Text:
        return "action_multi_nutrition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Collect intents predicted in the current message with their confidence
        latest_parse = tracker.latest_message.get("intent_ranking", [])
        detected_intents = [intent["name"] for intent in latest_parse if intent["name"] in nutrition_info]

        if not detected_intents:
            dispatcher.utter_message(text="I didn't understand. I can help with carbs, protein, diabetes, and nutrition myths.")
            return []

        # Combine answers for all detected intents
        combined_info = "\n\n".join([nutrition_info[intent] for intent in detected_intents])
        dispatcher.utter_message(text=combined_info)
        return []