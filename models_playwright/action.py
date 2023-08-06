import asyncio
from logger.logger import Logger
               
async def close_async(browser, context):
    await context.close()
    await browser.close()
    
def cancel_all_tasks(exception):
    Logger.warning('cancel_all_tasks', f'A task failed with: {exception}, canceling all tasks')
    tasks  = asyncio.all_tasks()
    current = asyncio.current_task()
    tasks.remove(current)
    for task in tasks:
        task.cancel()