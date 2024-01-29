from Features.Open import OpenExe
def MainTaskExecution(Query):
     try:
        if "open" in Query:
                Value = OpenExe(Query)
                return Value
        elif "visit" in Query:
                Value = OpenExe(Query)
                return Value
        elif "search" in Query:
                Value = OpenExe(Query)
                return Value
        elif "temperature" in Query:
                Value = OpenExe(Query)
                return Value
        elif "weather" in Query:
                Value = OpenExe(Query)
                return Value
        elif "present date" in Query or "current date" in Query or "what is the date" in Query or "whats the date" in Query or "what's the date" in Query or "what date it is" in Query or "what date is it" in Query:
            Value= OpenExe(Query)
            return Value 
        elif "present time" in Query or "current time" in Query or "what is the time" in Query or "whats the time" in Query or "what's the time" in Query or "what time it is" in Query or "what time is it" in Query:
            Value= OpenExe(Query)
            return Value 
        elif " date " in Query and " time " in Query:
            Value= OpenExe(Query)
            return Value 
     except:
         pass
