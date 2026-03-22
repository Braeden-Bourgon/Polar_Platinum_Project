#https://www.apriorit.com/dev-blog/768-ai-develop-smart-chatbots-using-python#cre
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

# for a large model, change the word 'base'
model_name = "microsoft/GODEL-v1_1-base-seq2seq"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

nickname = input('Your nickname: ')
# print('nChat (ask a question to start a conversation): ')

# for response_num in range(7):
#     # greedy search
#     # ask bot something
#     question = input('{}: '.format(nickname))
    
#     # encode the input and add end of string token
#     user_input = tokenizer.encode(question + tokenizer.eos_token, return_tensors="pt")
    
#     # concatenate new user input with the chat history
#     chatbot_input = torch.cat([chat_history, user_input], dim=-1) if response_num > 0 else user_input
    
#     # generate a response
#     chat_history = model.generate(
#         chatbot_input,
#         max_length=500,
#         pad_token_id=tokenizer.eos_token_id,
#     )
    
#     #print the output
#     chat = tokenizer.decode(chat_history[:, chatbot_input.shape[-1]:][0], skip_special_tokens=True)
    
#     print(f"Bot: {chat}")


# print('\nBetterChat (ask a question to start a conversation): ')

# for response_num in range(7):
#     #beam search
#     # ask bot something
#     question = input('{}: '.format(nickname))
    
#     # encode the input and add end of string token
#     user_input = tokenizer.encode(question + tokenizer.eos_token, return_tensors="pt")
    
#     # concatenate new user input with the chat history
#     chatbot_input = torch.cat([better_chat_history, user_input], dim=-1) if response_num > 0 else user_input
    
#     # generate a response
#     better_chat_history = model.generate(
#         chatbot_input,
#         max_length=500,
#         num_beams=4,
#         early_stopping=True,
#         pad_token_id=tokenizer.eos_token_id,
#     )
    
#     #print the output
#     chat = tokenizer.decode(better_chat_history[:, chatbot_input.shape[-1]:][0], skip_special_tokens=True)
    
#     print(f"Bot: {chat}")

print('SampleMethodChat (ask a question to start a conversation): ')

for response_num in range(7):
    # sample method
    # ask bot something
    question = input('{}: '.format(nickname))
    
    # encode the input
    user_input = tokenizer.encode(question + tokenizer.eos_token, return_tensors="pt")
    
    # concatenate the user input with the chat history
    chatbot_input = torch.cat([sample_chat_history, user_input], dim=-1) if response_num > 0 else user_input
    
    # generate a response
    sample_chat_history = model.generate(
        chatbot_input,
        max_length=1000,
        do_sample=True,
        top_k=70,
        temperature=0.7,
        pad_token_id=tokenizer.eos_token_id,
    )
    
    # print the output
    chat = tokenizer.decode(sample_chat_history[:, chatbot_input.shape[-1]:][0], skip_special_tokens=True)
    
    print(f"Bot: {chat}")
print('BestChat (ask a question to start a conversation): ')

for response_num in range(7):
    
    # ask bot something
    question = input('{}: '.format(nickname))
    
    # encode the input
    user_input = tokenizer.encode(question + tokenizer.eos_token, return_tensors="pt")
    
    # concatenate the user input with the chat history
    chatbot_input = torch.cat([best_chat_history, user_input], dim=-1) if response_num > 0 else user_input
    
    # generate a response
    best_chat_history = model.generate(
        chatbot_input,
        max_length=1000,
        do_sample=True,
        top_k=70,
        top_p=0.95,
        temperature=0.7,
        pad_token_id=tokenizer.eos_token_id,
    )
    
    # print the output
    chat = tokenizer.decode(best_chat_history[:, chatbot_input.shape[-1]:][0], skip_special_tokens=True)
    
    print(f"Bot: {chat}")