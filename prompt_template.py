
def point_zh_no_ref_no_criteria(data_dict, label_type):
    instruct = data_dict["instruction"]
    response = data_dict["response"]

    '''input'''
    input = ""
    input += "### 任务描述\n"
    input += "给出一条用户指令和一条由模型生成的对该指令的回复，请你对该回复进行评价并给该回复打分。\n"
    input += "1.对该回复写一份详细的评价，用于评价该回复的质量。\n"
    input += f"2.写完评价后，给出一个1到{label_type}之间的整数得分，表示你对该回复的评价分数，分数越高表示回复质量越好。\n"
    input += "3.输出格式如下所示:\n{你对回复的评价}\n总评分:{你对回复的打分}\n"
    input += "4.严格按照格式生成，不要产生任何其他的开场白、结束语和解释。\n\n"

    input += "### 用户指令\n"
    input += instruct
    input += "\n\n"

    input += "### 待评价的回复\n"
    input += response
    input += "\n"

    return input


def point_en_no_ref_no_criteria(data_dict, label_type):
    instruct = data_dict["instruction"]
    response = data_dict["response"]

    '''input'''
    input = ""
    input += "### Task Description\n"
    input += "Given a user instruction and a model-generated response to that instruction, evaluate the response and score the response.\n"
    input += "1.Write a detailed critique on the response that will be used to evaluate the quality of the response.\n"
    input += f"2.After writing your critique, give an integer score between 1 and {label_type} to indicate your rating score for the response, with a higher score indicating a better quality response.\n"
    input += "3.The output format is shown below:\n{Your critique of the response}\nOverall score:{Your score for the response}\n"
    input += "4.Generated strictly according to the output format and do not generate any other openings, closings or explanations.\n\n"

    input += "### User instruction\n"
    input += instruct
    input += "\n\n"

    input += "### Response to be evaluated\n"
    input += response
    input += "\n"


    return input


def point_zh_no_ref_criteria(data_dict, label_type):

    instruct = data_dict["instruction"]
    response = data_dict["response"]
    criteria = data_dict["criteria"]

    '''input'''
    input = ""
    input += "### 任务描述\n"
    input += "给出一条用户指令、一条由模型生成的对该指令的回复、一些对回复进行评价的准则，请你依据评价准则对该回复进行评价并给该回复打分。\n"
    input += "1.依据评价准则对该回复写一份详细的评价，用于评价该回复的质量。\n"
    input += "2.按照评价准则的每一点，逐点对回复进行评价，不要遗漏任何评价准则点。对所有评价准则点评价后，最后给出一个总体评价。\n"
    input += f"3.写完评价后，给出一个1到{label_type}之间的整数得分，表示你对该回复的评价分数，分数越高表示回复质量越好。\n"
    input += "4.输出格式如下所示:\n{你对回复的评价}\n总评分:{你对回复的打分}\n"
    input += "5.严格按照格式生成，不要产生任何其他的开场白、结束语和解释。\n\n"

    input += "### 用户指令\n"
    input += instruct
    input += "\n\n"

    input += "### 待评价的回复\n"
    input += response
    input += "\n\n"

    input += "### 评价准则\n"
    input += criteria
    input += "\n"


    return input
    
def point_en_no_ref_criteria(data_dict, label_type):

    instruct = data_dict["instruction"]
    response = data_dict["response"]
    criteria = data_dict["criteria"]

    '''input'''
    input = ""
    input += "### Task Description\n"
    input += "Given a user instruction, a model-generated response to that instruction, and some criteria for evaluating the response, evaluate the response based on the evaluation criteria and score the response.\n"
    input += "1.Write a detailed critique on the response based on the evaluation criteria that will be used to evaluate the quality of the response.\n"
    input += "2.Critique the response point by point, following each point of the evaluation criteria, without missing any evaluation criteria points. After criticizing all evaluation criteria points, give a final overall critique.\n"
    input += f"3.After writing your critique, give an integer score between 1 and {label_type} to indicate your rating score for the response, with a higher score indicating a better quality response.\n"
    input += "4.The output format is shown below:\n{Your critique of the response}\nOverall score:{Your score for the response}\n"
    input += "5.Generated strictly according to the output format and do not generate any other openings, closings or explanations.\n\n"

    input += "### User instruction\n"
    input += instruct
    input += "\n\n"

    input += "### Response to be evaluated\n"
    input += response
    input += "\n\n"

    input += "### Evaluation criteria\n"
    input += criteria
    input += "\n"


    return input



def point_zh_ref_no_criteria(data_dict, label_type):
    instruct = data_dict["instruction"]
    response = data_dict["response"]
    ref_response = data_dict["ref_response"]

    '''input'''
    input = ""
    input += "### 任务描述\n"
    input += "给出一条用户指令、一条由模型生成的对该指令的回复，请你对该回复进行评价并给该回复打分。除此之外，还提供了一条满分参考回复供你参考。\n"
    input += "1.依据参考回复，对该回复写一份详细的评价，用于评价该回复的质量。\n"
    input += f"2.写完评价后，给出一个1到{label_type}之间的整数得分，表示你对该回复的评价分数，分数越高表示回复质量越好。\n"
    input += "3.输出格式如下所示:\n{你对回复的评价}\n总评分:{你对回复的打分}\n"
    input += "4.严格按照格式生成，不要产生任何其他的开场白、结束语和解释。\n\n"

    input += "### 用户指令\n"
    input += instruct
    input += "\n\n"

    input += "### 待评价的回复\n"
    input += response
    input += "\n\n"

    input += "### 满分参考回复\n"
    input += ref_response
    input += "\n"  

    return input


def point_en_ref_no_criteria(data_dict, label_type):
    instruct = data_dict["instruction"]
    response = data_dict["response"]
    ref_response = data_dict["ref_response"]


    '''input'''
    input = ""
    input += "### Task Description\n"
    input += "Given a user instruction and a model-generated response to that instruction, evaluate the response and score the response. In addition to this, a full score reference response is provided for your reference.\n"
    input += "1.Based on the referenced response, write a detailed critique on the response that will be used to evaluate the quality of the response.\n"
    input += f"2.After writing your critique, give an integer score between 1 and {label_type} to indicate your rating score for the response, with a higher score indicating a better quality response.\n"
    input += "3.The output format is shown below:\n{Your critique of the response}\nOverall score:{Your score for the response}\n"
    input += "4.Generated strictly according to the output format and do not generate any other openings, closings or explanations.\n\n"

    input += "### User instruction\n"
    input += instruct
    input += "\n\n"

    input += "### Response to be evaluated\n"
    input += response
    input += "\n\n"

    input += "### Full score reference response\n"
    input += ref_response
    input += "\n"  

    return input


def point_zh_ref_criteria(data_dict, label_type):

    instruct = data_dict["instruction"]
    response = data_dict["response"]
    ref_response = data_dict["ref_response"]
    criteria = data_dict["criteria"]


    '''input'''
    input = ""
    input += "### 任务描述\n"
    input += "给出一条用户指令、一条由模型生成的对该指令的回复、一些对回复进行评价的准则，请你依据评价准则对该回复进行评价并给该回复打分。除此之外，还提供了一条满分参考回复供你参考。\n"
    input += "1.依据评价准则和参考回复对该回复写一份详细的评价，用于评价该回复的质量。\n"
    input += "2.按照评价准则的每一点，逐点对回复进行评价，不要遗漏任何评价准则点。对所有评价准则点评价后，最后给出一个总体评价。\n"
    input += f"3.写完评价后，给出一个1到{label_type}之间的整数得分，表示你对该回复的评价分数，分数越高表示回复质量越好。\n"
    input += "4.输出格式如下所示:\n{你对回复的评价}\n总评分:{你对回复的打分}\n"
    input += "5.严格按照格式生成，不要产生任何其他的开场白、结束语和解释。\n\n"

    input += "### 用户指令\n"
    input += instruct
    input += "\n\n"

    input += "### 待评价的回复\n"
    input += response
    input += "\n\n"

    input += "### 满分参考回复\n"
    input += ref_response
    input += "\n\n"  

    input += "### 评价准则\n"
    input += criteria
    input += "\n"

    return input

def point_en_ref_criteria(data_dict, label_type):

    instruct = data_dict["instruction"]
    response = data_dict["response"]
    ref_response = data_dict["ref_response"]
    criteria = data_dict["criteria"]


    '''input'''
    input = ""
    input += "### Task Description\n"
    input += "Given a user instruction, a model-generated response to that instruction, and some criteria for evaluating the response, evaluate the response based on the evaluation criteria and score the response. In addition to this, a full score reference response is provided for your reference.\n"
    input += "1.Write a detailed critique on the response based on the evaluation criteria and referenced response that will be used to evaluate the quality of the response.\n"
    input += "2.Critique the response point by point, following each point of the evaluation criteria, without missing any evaluation criteria points. After criticizing all evaluation criteria points, give a final overall critique.\n"
    input += f"3.After writing your critique, give an integer score between 1 and {label_type} to indicate your rating score for the response, with a higher score indicating a better quality response.\n"
    input += "4.The output format is shown below:\n{Your critique of the response}\nOverall score:{Your score for the response}\n"
    input += "5.Generated strictly according to the output format and do not generate any other openings, closings or explanations.\n\n"

    input += "### User instruction\n"
    input += instruct
    input += "\n\n"

    input += "### Response to be evaluated\n"
    input += response
    input += "\n\n"

    input += "### Full score reference response\n"
    input += ref_response
    input += "\n\n"  

    input += "### Evaluation criteria\n"
    input += criteria
    input += "\n"


    return input



def pair_zh_no_ref_no_criteria(data_dict, label_type):

    instruct = data_dict["instruction"]
    response_1 = data_dict["response_1"]
    response_2 = data_dict["response_2"]


    '''input'''
    input = ""
    input += "### 任务描述\n"
    if label_type == 3:
        input += "给出一条用户指令和两条由模型生成的对该指令的回复，请你对这两条回复进行评价并判断哪一条回复更好或者是平局。\n"
    elif label_type == 2:
        input += "给出一条用户指令和两条由模型生成的对该指令的回复，请你对这两条回复进行评价并判断哪一条回复更好。\n"

    input += "1.对这两条回复写一份详细的对比评价，用于评价这两条回复的质量。\n"

    if label_type == 3:
        input += "2.写完评价后，给出你最终的判断，表示你认为哪一个回复更好或平局。\n"
    elif label_type == 2:
        input += "2.写完评价后，给出你最终的判断，表示你认为哪一个回复更好。\n"
    
    if label_type == 3:
        input += "3.输出格式如下所示:\n{你对两条回复的对比评价}\n最终判断:{回复A或者回复B或者平局}\n"
    elif label_type == 2:
        input += "3.输出格式如下所示:\n{你对两条回复的对比评价}\n最终判断:{回复A或者回复B}\n"

    input += "4.避免任何立场偏见。确保两个回复的顺序不会影响你的判断。不要让回复的长度影响你的判断。不要因为喜欢某个回复的名字影响你的判断。尽可能客观。\n"
    input += "5.严格按照格式生成，不要产生任何其他的开场白、结束语和解释。\n\n"

    input += "### 用户指令\n"
    input += instruct
    input += "\n\n"

    input += "### 待评价的回复A\n"
    input += response_1
    input += "\n\n"

    input += "### 待评价的回复B\n"
    input += response_2
    input += "\n"

    return input

def pair_en_no_ref_no_criteria(data_dict, label_type):

    instruct = data_dict["instruction"]
    response_1 = data_dict["response_1"]
    response_2 = data_dict["response_2"]

    '''input'''
    input = ""
    input += "### Task Description\n"
    if label_type == 3:
        input += "Given a user instruction and maybe an input and two model-generated responses to that instruction, evaluate the two responses and judge which response is better or a tie.\n"
    elif label_type == 2:
        input += "Given a user instruction and maybe an input and two model-generated responses to that instruction, evaluate the two responses and judge which response is better.\n"
    
    input += "1.Write a detailed comparative critique of the two responses that will be used to evaluate the quality of the two responses.\n"
    
    if label_type == 3:
        input += "2.After writing your critique, give your final judgment, indicating which response you think is better or a tie.\n"
    elif label_type == 2:
        input += "2.After writing your critique, give your final judgment, indicating which response you think is better.\n"
    
    if label_type == 3:
        input += "3.The output format is shown below:\n{Your comparative critique of the two responses}\nFinal judgment:{Response A or Response B or Tie}\n"
    elif label_type == 2:
        input += "3.The output format is shown below:\n{Your comparative critique of the two responses}\nFinal judgment:{Response A or Response B}\n"
    
    input += "4.Avoid any positional bias. Make sure the order of the two responses does not influence your judgment. Don't let the length of a response influence your judgment. Don't let liking the name of a particular response influence your judgment. Be as objective as possible.\n"
    input += "5.Generated strictly according to the output format and do not generate any other openings, closings or explanations.\n\n"

    input += "### User instruction\n"
    input += instruct
    input += "\n\n"

    if "input" in data_dict:
        input += "### Input\n"
        input += data_dict["input"]
        input += "\n\n"

    input += "### Response A to be evaluated\n"
    input += response_1
    input += "\n\n"

    input += "### Response B to be evaluated\n"
    input += response_2
    input += "\n"

    return input

def pair_zh_no_ref_criteria(data_dict, label_type):

    instruct = data_dict["instruction"]
    response_1 = data_dict["response_1"]
    response_2 = data_dict["response_2"]
    criteria = data_dict["criteria"]

    '''input'''
    input = ""
    input += "### 任务描述\n"
    if label_type == 3:
        input += "给出一条用户指令、两条由模型生成的对该指令的回复、一些对回复进行评价的准则，请你依据评价准则对这两条回复进行评价并判断哪一条回复更好或者是平局。\n"
    elif label_type == 2:
        input += "给出一条用户指令、两条由模型生成的对该指令的回复、一些对回复进行评价的准则，请你依据评价准则对这两条回复进行评价并判断哪一条回复更好。\n"
    
    input += "1.依据评价准则对这两条回复写一份详细的对比评价，用于评价这两条回复的质量。\n"
    input += "2.按照评价准则的每一点，逐点对这两条回复进行对比评价，不要遗漏任何评价准则点。对所有评价准则点评价后，最后给出一个总体评价。\n"
    
    if label_type == 3:
        input += "3.写完评价后，给出你最终的判断，表示你认为哪一个回复更好或平局。\n"
    elif label_type == 2:
        input += "3.写完评价后，给出你最终的判断，表示你认为哪一个回复更好。\n"

    if label_type == 3:
        input += "4.输出格式如下所示:\n{你对两条回复的对比评价}\n最终判断:{回复A或者回复B或者平局}\n"
    elif label_type == 2:
        input += "4.输出格式如下所示:\n{你对两条回复的对比评价}\n最终判断:{回复A或者回复B}\n"

    input += "5.避免任何立场偏见。确保两个回复的顺序不会影响你的判断。不要让回复的长度影响你的判断。不要因为喜欢某个回复的名字影响你的判断。尽可能客观。\n"
    input += "6.严格按照格式生成，不要产生任何其他的开场白、结束语和解释。\n\n"

    input += "### 用户指令\n"
    input += instruct
    input += "\n\n"

    input += "### 待评价的回复A\n"
    input += response_1
    input += "\n\n"

    input += "### 待评价的回复B\n"
    input += response_2
    input += "\n\n"

    input += "### 评价准则\n"
    input += criteria
    input += "\n"

    return input

def pair_en_no_ref_criteria(data_dict, label_type):

    instruct = data_dict["instruction"]
    response_1 = data_dict["response_1"]
    response_2 = data_dict["response_2"]
    criteria = data_dict["criteria"]


    '''input'''
    input = ""
    input += "### Task Description\n"

    if label_type == 3:
        input += "Given a user instruction, two model-generated responses to that instruction, and some criteria for critiquing the responses, evaluate the two responses based on the evaluation criteria and judge which response is better or a tie.\n"
    elif label_type == 2:
        input += "Given a user instruction, two model-generated responses to that instruction, and some criteria for critiquing the responses, evaluate the two responses based on the evaluation criteria and judge which response is better.\n"
    
    input += "1.Write a detailed comparative critique of the two responses based on the evaluation criteria that will be used to evaluate the quality of the two responses.\n"
    input += "2.Critique the two responses point by point, following each point of the evaluation criteria, without missing any evaluation criteria points. After criticizing all evaluation criteria points, give a final overall critique.\n"
    
    if label_type == 3:
        input += "3.After writing your critique, give your final judgment, indicating which response you think is better or a tie.\n"
    elif label_type == 2:
        input += "3.After writing your critique, give your final judgment, indicating which response you think is better.\n"
    
    if label_type == 3:
        input += "4.The output format is shown below:\n{Your comparative critique of the two responses}\nFinal judgment:{Response A or Response B or Tie}\n"
    elif label_type == 2:
        input += "4.The output format is shown below:\n{Your comparative critique of the two responses}\nFinal judgment:{Response A or Response B}\n"
    
    input += "5.Avoid any positional bias. Make sure the order of the two responses does not influence your judgment. Don't let the length of a response influence your judgment. Don't let liking the name of a particular response influence your judgment. Be as objective as possible.\n"
    input += "6.Generated strictly according to the output format and do not generate any other openings, closings or explanations.\n\n"

    input += "### User instruction\n"
    input += instruct
    input += "\n\n"

    input += "### Response A to be evaluated\n"
    input += response_1
    input += "\n\n"

    input += "### Response B to be evaluated\n"
    input += response_2
    input += "\n\n"

    input += "### Evaluation criteria\n"
    input += criteria
    input += "\n"


    return input

def pair_zh_ref_no_criteria(data_dict, label_type):

    instruct = data_dict["instruction"]
    response_1 = data_dict["response_1"]
    response_2 = data_dict["response_2"]
    ref_response = data_dict["ref_response"]


    '''input'''
    input = ""
    input += "### 任务描述\n"
    if label_type == 3:
        input += "给出一条用户指令、两条由模型生成的对该指令的回复，请你对这两条回复进行评价并判断哪一条回复更好或者是平局。除此之外，还提供了一条满分参考回复供你参考。\n"
    elif label_type == 2:
        input += "给出一条用户指令、两条由模型生成的对该指令的回复，请你对这两条回复进行评价并判断哪一条回复更好。除此之外，还提供了一条满分参考回复供你参考。\n"
    
    input += "1.依据参考回复对这两条回复写一份详细的对比评价，用于评价这两条回复的质量。\n"
    
    if label_type == 3:
        input += "2.写完评价后，给出你最终的判断，表示你认为哪一个回复更好或平局。\n"
    elif label_type == 2:
        input += "2.写完评价后，给出你最终的判断，表示你认为哪一个回复更好。\n"

    if label_type == 3:
        input += "3.输出格式如下所示:\n{你对两条回复的对比评价}\n最终判断:{回复A或者回复B或者平局}\n"
    elif label_type == 2:
        input += "3.输出格式如下所示:\n{你对两条回复的对比评价}\n最终判断:{回复A或者回复B}\n"

    input += "4.避免任何立场偏见。确保两个回复的顺序不会影响你的判断。不要让回复的长度影响你的判断。不要因为喜欢某个回复的名字影响你的判断。尽可能客观。\n"
    input += "5.严格按照格式生成，不要产生任何其他的开场白、结束语和解释。\n\n"

    input += "### 用户指令\n"
    input += instruct
    input += "\n\n"

    input += "### 待评价的回复A\n"
    input += response_1
    input += "\n\n"

    input += "### 待评价的回复B\n"
    input += response_2
    input += "\n\n"

    input += "### 满分参考回复\n"
    input += ref_response
    input += "\n"  

    return input


def pair_en_ref_no_criteria(data_dict, label_type):

    instruct = data_dict["instruction"]
    response_1 = data_dict["response_1"]
    response_2 = data_dict["response_2"]
    ref_response = data_dict["ref_response"]

    '''input'''
    input = ""
    input += "### Task Description\n"
    if label_type == 3:
        input += "Given a user instruction and two model-generated responses to that instruction, evaluate the two responses and judge which response is better or a tie. In addition to this, a full score reference response is provided for your reference.\n"
    elif label_type == 2:
        input += "Given a user instruction and two model-generated responses to that instruction, evaluate the two responses and judge which response is better. In addition to this, a full score reference response is provided for your reference.\n"
    
    input += "1.Write a detailed comparative critique of the two responses based on the referenced response that will be used to evaluate the quality of the two responses.\n"
    
    if label_type == 3:
        input += "2.After writing your critique, give your final judgment, indicating which response you think is better or a tie.\n"
    elif label_type == 2:
        input += "2.After writing your critique, give your final judgment, indicating which response you think is better.\n"
    
    if label_type == 3:
        input += "3.The output format is shown below:\n{Your comparative critique of the two responses}\nFinal judgment:{Response A or Response B or Tie}\n"
    elif label_type == 2:
        input += "3.The output format is shown below:\n{Your comparative critique of the two responses}\nFinal judgment:{Response A or Response B}\n"
    
    input += "4.Avoid any positional bias. Make sure the order of the two responses does not influence your judgment. Don't let the length of a response influence your judgment. Don't let liking the name of a particular response influence your judgment. Be as objective as possible.\n"
    input += "5.Generated strictly according to the output format and do not generate any other openings, closings or explanations.\n\n"


    input += "### User instruction\n"
    input += instruct
    input += "\n\n"

    input += "### Response A to be evaluated\n"
    input += response_1
    input += "\n\n"

    input += "### Response B to be evaluated\n"
    input += response_2
    input += "\n\n"

    input += "### Full score reference response\n"
    input += ref_response
    input += "\n"  


    return input


def pair_zh_ref_criteria(data_dict, label_type):

    instruct = data_dict["instruction"]
    response_1 = data_dict["response_1"]
    response_2 = data_dict["response_2"]
    criteria = data_dict["criteria"]
    ref_response = data_dict["ref_response"]


    '''input'''
    input = ""
    input += "### 任务描述\n"
    if label_type == 3:
        input += "给出一条用户指令、两条由模型生成的对该指令的回复、一些对回复进行评价的准则，请你依据评价准则对这两条回复进行评价并判断哪一条回复更好或者是平局。除此之外，还提供了一条满分参考回复供你参考。\n"
    elif label_type == 2:
        input += "给出一条用户指令、两条由模型生成的对该指令的回复、一些对回复进行评价的准则，请你依据评价准则对这两条回复进行评价并判断哪一条回复更好。除此之外，还提供了一条满分参考回复供你参考。\n"
    
    input += "1.依据评价准则和参考回复对这两条回复写一份详细的对比评价，用于评价这两条回复的质量。\n"
    input += "2.按照评价准则的每一点，逐点对这两条回复进行对比评价，不要遗漏任何评价准则点。对所有评价准则点评价后，最后给出一个总体评价。\n"
    
    if label_type == 3:
        input += "3.写完评价后，给出你最终的判断，表示你认为哪一个回复更好或平局。\n"
    elif label_type == 2:
        input += "3.写完评价后，给出你最终的判断，表示你认为哪一个回复更好。\n"

    if label_type == 3:    
        input += "4.输出格式如下所示:\n{你对两条回复的对比评价}\n最终判断:{回复A或者回复B或者平局}\n"
    elif label_type == 2:
        input += "4.输出格式如下所示:\n{你对两条回复的对比评价}\n最终判断:{回复A或者回复B}\n"

    input += "5.避免任何立场偏见。确保两个回复的顺序不会影响你的判断。不要让回复的长度影响你的判断。不要因为喜欢某个回复的名字影响你的判断。尽可能客观。\n"
    input += "6.严格按照格式生成，不要产生任何其他的开场白、结束语和解释。\n\n"

    input += "### 用户指令\n"
    input += instruct
    input += "\n\n"

    input += "### 待评价的回复A\n"
    input += response_1
    input += "\n\n"

    input += "### 待评价的回复B\n"
    input += response_2
    input += "\n\n"

    input += "### 满分参考回复\n"
    input += ref_response
    input += "\n\n"  

    input += "### 评价准则\n"
    input += criteria
    input += "\n"

    return input


def pair_en_ref_criteria(data_dict, label_type):

    instruct = data_dict["instruction"]
    response_1 = data_dict["response_1"]
    response_2 = data_dict["response_2"]
    criteria = data_dict["criteria"]
    ref_response = data_dict["ref_response"]

    '''input'''
    input = ""
    input += "### Task Description\n"

    if label_type == 3:  
        input += "Given a user instruction, two model-generated responses to that instruction, and some criteria for critiquing the responses, evaluate the two responses based on the evaluation criteria and judge which response is better or a tie. In addition to this, a full score reference response is provided for your reference.\n"
    elif label_type == 2:
        input += "Given a user instruction, two model-generated responses to that instruction, and some criteria for critiquing the responses, evaluate the two responses based on the evaluation criteria and judge which response is better. In addition to this, a full score reference response is provided for your reference.\n"
    
    input += "1.Write a detailed comparative critique on the two response based on the evaluation criteria and referenced response that will be used to evaluate the quality of the two responses.\n"
    input += "2.Critique the two responses point by point, following each point of the evaluation criteria, without missing any evaluation criteria points. After criticizing all evaluation criteria points, give a final overall critique.\n"
    
    if label_type == 3: 
        input += "3.After writing your critique, give your final judgment, indicating which response you think is better or a tie.\n"
    elif label_type == 2:
        input += "3.After writing your critique, give your final judgment, indicating which response you think is better.\n"
    
    if label_type == 3: 
        input += "4.The output format is shown below:\n{Your comparative critique of the two responses}\nFinal judgment:{Response A or Response B or Tie}\n"
    elif label_type == 2:
        input += "4.The output format is shown below:\n{Your comparative critique of the two responses}\nFinal judgment:{Response A or Response B}\n"
    
    input += "5.Avoid any positional bias. Make sure the order of the two responses does not influence your judgment. Don't let the length of a response influence your judgment. Don't let liking the name of a particular response influence your judgment. Be as objective as possible.\n"
    input += "6.Generated strictly according to the output format and do not generate any other openings, closings or explanations.\n\n"

    input += "### User instruction\n"
    input += instruct
    input += "\n\n"

    input += "### Response A to be evaluated\n"
    input += response_1
    input += "\n\n"

    input += "### Response B to be evaluated\n"
    input += response_2
    input += "\n\n"

    input += "### Full score reference response\n"
    input += ref_response
    input += "\n\n"  

    input += "### Evaluation criteria\n"
    input += criteria
    input += "\n"


    return input


def get_prompt(config_mode, config_lang, have_ref, have_criteria, data_dict, label_type):
    if config_mode == "point":
        if config_lang == "zh":
            if have_ref == 1 and have_criteria == 1:
                prompt = point_zh_ref_criteria(data_dict, label_type)
            elif have_ref == 1 and have_criteria == 0:
                prompt = point_zh_ref_no_criteria(data_dict, label_type)
            elif have_ref == 0 and have_criteria == 1:
                prompt = point_zh_no_ref_criteria(data_dict, label_type)
            elif have_ref == 0 and have_criteria == 0:
                prompt = point_zh_no_ref_no_criteria(data_dict, label_type)
        elif config_lang == "en":
            if have_ref == 1 and have_criteria == 1:
                prompt = point_en_ref_criteria(data_dict, label_type)
            elif have_ref == 1 and have_criteria == 0:
                prompt = point_en_ref_no_criteria(data_dict, label_type)
            elif have_ref == 0 and have_criteria == 1:
                prompt = point_en_no_ref_criteria(data_dict, label_type)
            elif have_ref == 0 and have_criteria == 0:
                prompt = point_en_no_ref_no_criteria(data_dict, label_type)
    elif config_mode == "pair":
        if config_lang == "zh":
            if have_ref == 1 and have_criteria == 1:
                prompt = pair_zh_ref_criteria(data_dict, label_type)
            elif have_ref == 1 and have_criteria == 0:
                prompt = pair_zh_ref_no_criteria(data_dict, label_type)
            elif have_ref == 0 and have_criteria == 1:
                prompt = pair_zh_no_ref_criteria(data_dict, label_type)
            elif have_ref == 0 and have_criteria == 0:
                prompt = pair_zh_no_ref_no_criteria(data_dict, label_type)
        elif config_lang == "en":
            if have_ref == 1 and have_criteria == 1:
                prompt = pair_en_ref_criteria(data_dict, label_type)
            elif have_ref == 1 and have_criteria == 0:
                prompt = pair_en_ref_no_criteria(data_dict, label_type)
            elif have_ref == 0 and have_criteria == 1:
                prompt = pair_en_no_ref_criteria(data_dict, label_type)
            elif have_ref == 0 and have_criteria == 0:
                prompt = pair_en_no_ref_no_criteria(data_dict, label_type)

    return prompt

