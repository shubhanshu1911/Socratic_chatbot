import React, { useState } from 'react';
import { askQuestion } from './api';

const ChatBox = () => {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState('');
    const [studentName, setStudentName] = useState('John Doe');

    const sendMessage = async () => {
        const response = await askQuestion(studentName, input);
        setMessages([...messages, { sender: 'student', text: input }, { sender: 'assistant', text: response.data.response }]);
        setInput('');
    };

    return (
        <div>
            <div className="chat">
                {messages.map((msg, index) => (
                    <div key={index} className={`message ${msg.sender}`}>
                        {msg.text}
                    </div>
                ))}
            </div>
            <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
            />
        </div>
    );
};

export default ChatBox;
