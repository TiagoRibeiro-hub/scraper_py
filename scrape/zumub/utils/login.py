import asyncio
from logger import Log

class Login:
    def __init__(self):  
        self.modal_login = '[data-target="#myModalLogin"]'
        self.email = '#login-email-address'    
        self.password = '#login-password'    
        self.remember = '#chkRemember'   
        self.submit = 'xpath=//*[@id="loginForm"]/button'
        self.cookies = '#acceptCookies' 
        self.popup_create_subscribtion = '#popup_create_subscribtion' 
    
    async def submit_async(self, page, email, password): 
        try: 
            Log.info('LOGIN', 'Login submit started')             
            # * get popup create subscribtion selector
            popup_create_subscribtion_task = page.query_selector(self.popup_create_subscribtion)

            # * open login form
            await page.locator(self.modal_login).click() 
            await asyncio.sleep(3)
                
            # * get remember selector
            chkRemember_task = page.query_selector(self.remember)
                
            # * remove popup create subscribtion
            popup_create_subscribtion = await popup_create_subscribtion_task  
            if popup_create_subscribtion:
                await popup_create_subscribtion.evaluate('el => el.remove()')
                
            # * user name and pwd
            await page.locator(self.email).fill(email) 
            await asyncio.sleep(2)
            await page.locator(self.password).fill(password) 
            await asyncio.sleep(2)
                            
            # * accept cookies
            await page.locator(self.cookies).click()
            await asyncio.sleep(2)
            
            # * uncheck rember 
            chkRemember = await chkRemember_task
            if chkRemember:
                await chkRemember.evaluate('el => el.checked=false')           
            await asyncio.sleep(2)  
                
            # * submit form
            await page.locator(self.submit).click()
            await asyncio.sleep(3)
            Log.info('LOGIN', 'Login is complete') 
        except Exception as e:
            Log.critical('LOGIN', f'Login as failed, {e}')          
            raise Exception(e)  
            