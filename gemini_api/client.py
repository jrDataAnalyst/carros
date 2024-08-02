import google.generativeai as genai

API_KEY = 'AIzaSyBjSqqdPWrhyernlkQczX8YWDAg8qdbUVA'

genai.configure(api_key=API_KEY)


def get_car_ai_bio(model, brand, year):
    message = ''''
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas desse modelo.
    Descreva especificações técnicas desse modelo de carro.
    '''
    message = message.format(brand, model, year)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(message)
    return response.text