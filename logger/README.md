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
- default => '%(asctime)s: %(levelname)s - %(message)s'
### meaning
- %(asctime)s => DEBUG 
- %(levelname)s => WARNING
- %(message)s' => log message

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