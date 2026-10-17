import datetime


class TransactionLogger:

    def __init__(self, filename: str):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, mode="a", encoding="utf-8")
        self.log("Transaction session started.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.log(f"Error occurred: {exc_val}")
        else:
            self.log("Transaction session finished successfully.")

        if self.file:
            self.file.close()
        return True

    def log(self, message: str):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.file.write(f"[{timestamp}] {message}\n")


with TransactionLogger("server.log") as logger:
    logger.log("Connecting to the payment gateway...")
    logger.log("Processing user deposit of $150.")

   
    raise ValueError("Database connection lost during commitment.")





class ExecutionTimer:

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        duration = time.time() - self.start_time
        print(f"Execution took: {duration:.4f} seconds")



with ExecutionTimer():
    
    time.sleep(0.5)