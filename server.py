import neuralintents
from functions import mappings


bot = neuralintents.GenericAssistant("intents.json", mappings, "model")
bot.train_model()
bot.save_model()