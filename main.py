import re


class Vault:
    INTENTS = {
        r'\b(atualizar|alterar|atualização|forma de pagamento|informações de pagamento)\b': 'PaymentIntent',
        r'\b(status|acompanhar|rastrear|pedido)\b': 'OrderIntent'

    }

    ACTIONS = {
        'PaymentIntent': 'Para atualizar suas informações de pagamento, acesse a página de configurações de pagamento em nosso site.',
        'OrderIntent': 'Para acompanhar o status do seu pedido, faça login em sua conta e acesse a área de pedidos do nosso site.'
    }


class Intent:
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def __str__(self):
        return f'{self.name}'


class IntentRecognizer:
    def __init__(self, intents):
        self.intents = intents

    def recognize(self, text):
        for intent, name in self.intents.items():
            if re.search(intent, text, re.IGNORECASE):
                return Intent(name, text)

        return None


class IntentHandler:
    def __init__(self, intents):
        self.intents = intents

    def handle(self, intent):
        if intent.name in self.intents:
            return self.intents[intent.name]

        return None


def main():
    intents = Vault.INTENTS
    actions = Vault.ACTIONS

    intent_recognizer = IntentRecognizer(intents)
    intent_handler = IntentHandler(actions)

    while True:
        text = input('>> ')

        if text == 'sair':
            print('Indo ali...')
            break

        if intent := intent_recognizer.recognize(text):
            action = intent_handler.handle(intent)
            print(action)
        else:
            print('Não entendi o que você disse.')


if __name__ == '__main__':
    main()
