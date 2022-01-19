#!python3
# 生成随机的测验试卷文件
# 键入你是一位地理老师，班上有35名学生，你希望进行美国各州首府的一个小测验。
# 不妙的是，班里有几个坏蛋，你无法确信学生不会作弊。你希望随机调整问题的次序，
# 这样每份试卷都是独一无二的，这让任何人都不能从其他人那里抄袭答案。当然，手工完成这件事又费时又无聊。
# 下面是程序所做的事
# 1.创建35份不同的测验试卷
# 2.位每份试卷创建50个多重选择题，次序随机
# 3.为每个问题提供一个正确答案和3个随机的错误答案，次序随机
# 4.将测验试卷写到35个文本文件中
# 5.将答案写道35个文本文件中
# 这将意味着代码需要做下面的事：
# 1.将州和它们的首府保存在一个字典中
# 2.针对测验文本文件和答案文本文件，调用open()、write()和close()
# 3.利用random.shuffle()随机调整问题和多重选项的次序
import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# 35个文本文件
for quizNum in range(35):
    quizFile = open('D:\\Virtual\\PythonLearn\\chapter8\\CapitalsQuiz\\capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('D:\\Virtual\\PythonLearn\\chapter8\\CapitalsQuiz\\capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # Shuffle the order of states
    states = list(capitals.keys())
    random.shuffle(states)  # 对传入的列表随机排序

    # Loop through all 50 states，making a question for each。
    for questionNum in range(50):
        
        # Get right and wrong answers.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)   # 第一个参数是你希望选择的列表，第二个参数是：你希望选择的值的个数
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # Write the question and the answer options to the quiz file
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n\n')

        # Write the key to a file.
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()