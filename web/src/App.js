import * as React from 'react'
import {Lrc} from 'lrc-kit';
import logo from './logo.svg';
import './App.css';

const lrc = `[ver:v1.0]
[ti:6488979]
[00:00.78]国王与乞丐-杨宗纬&华晨宇
[00:14.01]怎么了 怎么了
[00:17.19]一份爱失去了光泽
[00:20.18]面对面 背对背
[00:23.26]反复挣扎怎么都痛
[00:27.10]以为爱坚固像石头
[00:30.00]谁知一秒钟就碎落
[00:33.42]难道心痛都要不断打磨
[00:39.25]抱紧你的我比国王富有
[00:46.31]曾多么快乐
[00:52.15]失去你的我比乞丐落魄
[00:59.38]痛多么深刻
[01:05.71]噢 喔 噢 喔
[01:12.40]噢 喔 噢 喔
[01:18.87]谁哭着谁笑着
[01:21.64]一人分饰两个角色
[01:24.93]越执迷越折磨
[01:28.18]回忆还在煽风点火
[01:31.85]明知往前就会坠落
[01:34.87]抱着遗憾重返寂寞
[01:38.16]爱到最后究竟还剩什么
[01:43.95]抱紧你的我比国王富有
[01:51.67]曾多么快乐
[01:57.12]失去你的我比乞丐落魄
[02:04.25]痛多么深刻
[02:11.51]当一切 结束了 安静了 过去了
[02:17.74]为什么 还拥有 一万个 舍不得
[02:26.58]喔 喔
[02:36.96]谁又能感受
[02:42.58]回忆里的我比国王富有
[02:50.00]奢侈的快乐
[02:55.43]失去你以后比乞丐落魄
[03:06.18]心痛如刀割
[03:13.46]怀念那时你安静陪着我
[03:19.79]柔软时光里最美的挥霍
[03:28.95]爱有多快乐
[03:33.74]痛有多深刻
[03:40.21]痛有多深刻
`
function App() {
    const lyrics = Lrc.parse(lrc).lyrics
    const [vars] = React.useState({start: Date.now()/1e3, line: 0})
    const [index, setIndex] = React.useState(0)
    React.useEffect(() => {
        const id = setInterval(()=> {
            const total = Date.now()/1e3 - vars.start
            if (vars.line<lyrics.length-1 && total > lyrics[vars.line+1].timestamp) {
                setIndex(i=>i+1)
                vars.line++
            }
        }, 1000)
        return () => clearInterval(id)
    }, [])

    return (
        <div className="App">
        {lyrics.map((e,i)=> {
            return i===index?
                <p key={i}><b>{e.timestamp}:{e.content}</b></p>:
                <p key={i}>{e.timestamp}:{e.content}</p>
        })}        
        </div>
    );
}

export default App;
