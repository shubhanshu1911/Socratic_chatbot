import axios from 'axios';

export const askQuestion = async (studentName, question) => {
    return axios.post('http://localhost:8000/ask', { student_name: studentName, question });
};
