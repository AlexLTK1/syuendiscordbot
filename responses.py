def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there!'
    
    if p_message == '!抽卡':
        return str(random.randInt(1,100))
    
    if p_message == '!help':
        return "'This is a help message that you can modify.'"
    
    return "你到底在說甚麼呀:skull: "