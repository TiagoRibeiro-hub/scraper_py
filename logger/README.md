# Docs
-https://docs.python.org/3/library/logging.html

# config file:
- It must be in the root directory => config.yaml
- example: (to use default valuessta)
    logger: 
        path: 
        file_input_format:
        console_level: 
        log_file_level:

## path:
### where the log files will be saved
- default => root directory/logs
## file input format:
- default => '%(asctime)s - %(levelname)s - %(name)s -> %(message)s (%(filename)s:%(lineno)d)'
### meaning
- %(asctime)s => DEBUG 
- %(levelname)s => WARNING
- %(name)s => logger name
- %(message)s' => log message
- %(filename)s => file name
- %(lineno)d => linha do log

## levels:
## console level:
- default DEBUG

## log file level:
- default WARNING

### from which level start writing logs
- 0 (default)
- 1 (DEBUG)
- 2 (INFO)
- 3 (WARNING)
- 4 (ERROR)
- 5 (CRITICAL)