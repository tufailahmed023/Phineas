css = '''
<style>
.chat-message {
    padding: 1.5rem;
    border-radius: 1rem;
    margin-bottom: 1.2rem;
    display: flex;
    align-items: center;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease-in-out;
}
.chat-message.user {
    background: linear-gradient(135deg, #2e3b4e, #3a465e);
    border-left: 5px solid #4CAF50;
}
.chat-message.bot {
    background: linear-gradient(135deg, #4a5568, #5a6a82);
    border-left: 5px solid #f39c12;
}
.chat-message .avatar {
    width: 15%;
    display: flex;
    align-items: center;
    justify-content: center;
}
.chat-message .avatar img {
    max-width: 70px;
    max-height: 70px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid rgba(255, 255, 255, 0.3);
}
.chat-message .message {
    width: 85%;
    padding: 0 1.5rem;
    color: #fff;
    font-size: 1rem;
    line-height: 1.4;
}
</style>
'''
bot_template = '''

<!-- Bot Message -->
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://upload.wikimedia.org/wikipedia/en/6/60/Phineas_Flynn.png" alt="Phineas Avatar">
    </div>
    <div class="message">{{MSG}}</div>
</div>

'''

user_template = '''

<!-- User Message -->
<div class="chat-message user">
    <div class="avatar">
        <img src="https://upload.wikimedia.org/wikipedia/commons/3/3b/Tom_Cruise_by_Gage_Skidmore_2.jpg" alt="User Avatar">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
