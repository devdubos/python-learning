def simple_cube_generator(limit):
    """Yields cubes of numbers one by one without keeping a huge list in memory."""
    print("  [Gen 1] Starting generation...")
    for i in range(1, limit + 1):
        yield i ** 3  


print("--- Example 1: Extracting data using next() ---")
cubes = simple_cube_generator(3)

print(f"Received: {next(cubes)}")  
print(f"Received: {next(cubes)}") 
print(f"Received: {next(cubes)}")  





def EchoBot():
    """Using yield to receive data from the outside world."""
    print("  [Bot] Hello! I am ready to repeat your words.")
    while True:
        
        user_message = yield
        if user_message == "bye":
            print("  [Bot] Alright, catch you later!")
            break
        print(f"  [Bot] You said: '{user_message}'")


print("\n--- Example 2: Sending data using .send() ---")
bot = EchoBot()

next(bot)  
bot.send("Hello, how are you?")  
bot.send("Learning Python")
try:
    bot.send("bye")  
except StopIteration:
    print("Generator-bot has successfully finished.")




def sub_task(name):
    """A small sub-generator performing individual steps."""
    yield f"[{name}] Step 1"
    yield f"[{name}] Step 2"


def main_orchestrator():
    """The main generator that delegates control to sub-generators."""
    print("  [Main] Starting orchestration...")
    yield from sub_task("Subtask A")
    yield from sub_task("Subtask B")
    print("  [Main] All tasks completed!")


print("\n--- Example 3: Delegation using yield from ---")
orchestrator = main_orchestrator()
for step in orchestrator:
    print(f"Received in loop: {step}")






def raw_logs_generator(data):
    with open (data,'r', encoding='utf-8') as file:
        for line in file:
            if bool(line.strip()) == True:
                yield line

def critical_filter_generator(input_stream):
    for line in input_stream:
        clean_line = line.strip().lower()
        if "critical" in clean_line or "error" in clean_line:
            yield line

def alert_formatter_generator(filter_stream):
    for line in filter_stream:
        line = "🚨" + line.strip().upper()
        yield line




input_stream = raw_logs_generator(data)
filter_stream = critical_filter_generator(input_stream)
finish_stream = alert_formatter_generator(filter_stream)


for line in finish_stream:
    print(line)



