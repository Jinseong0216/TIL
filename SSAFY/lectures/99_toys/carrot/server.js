// server.js
const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const cors = require('cors');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

app.use(cors());  // CORS 설정 추가

// 소켓 연결 이벤트
io.on('connection', (socket) => {
    console.log('클라이언트 연결됨:', socket.id);

    // 클라이언트에서 클릭 이벤트 수신
    socket.on('shakeCarrot', () => {
        console.log('당근 흔들기 이벤트 받음');
        // 모든 클라이언트에게 당근 흔들기 이벤트 전송
        io.emit('shakeCarrot');
    });

    socket.on('disconnect', () => {
        console.log('클라이언트 연결 종료:', socket.id);
    });
});

server.listen(3000, () => {
    console.log('서버가 포트 3000에서 실행 중입니다.');
});
