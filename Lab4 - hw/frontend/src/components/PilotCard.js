import { FastAverageColor } from 'fast-average-color';
import './PilotCard.css';
import { useEffect, useState } from 'react';


export default function PilotCard({pilot}) {
    const [backgroundColor, setBackgroundColor] = useState('white');
    const [dark, setDark] = useState(true);
    const [team, setTeam] = useState({});
    const [score, setScore] = useState(pilot.score);

    useEffect(() => {
        new FastAverageColor().getColorAsync(pilot.image_url)
        .then(color => {
            const v = color.value.map(v => 255 - v);
            setBackgroundColor(`rgb(${v[0]}, ${v[1]}, ${v[2]})`);
            setDark(color.isDark);
        })
        .catch(e => console.error(e));
    }, []);

    useEffect(() => {
        fetch(`http://localhost:8002/teams/${pilot.extra_info.team_id}`)
        .then(response => response.json())
        .then(_team => {
            setTeam(_team);
        })
        .catch(error => console.error(error));
    }, []);

    useEffect(() => {
        setInterval(() => {
            fetch(`http://localhost:8003/scores/${pilot._id}`)
            .then(response => response.json())
            .then(_score => {
                setScore(_score);
            })
            .catch(error => console.error(error));
        }, 60000);
    }, []);

    const info = Object.entries(pilot.extra_info)
    .filter(([key, _]) => !key.endsWith('_id'))
    .map(([key, value]) => {
        return <div key={key} style={{display: 'flex', justifyContent: 'space-between'}}>
            <p>{key}</p>
            <p>{value}</p>
        </div>;
    });
    
    info.push(
        <div key='team' style={{display: 'flex', justifyContent: 'space-between'}}>
            <p>Team</p>
            <p>{team.name}</p>
        </div>
    );

    return (
        <div className='pilotCard' style={{backgroundColor, color: dark ? 'black' : 'white'}}>
            <div className='content'>
                <img alt={pilot.last_name} style={{width: '100%'}} src={pilot.image_url} />
                <div style={{display: 'flex', justifyContent: 'space-between'}}>
                    <div className='nameGroup'>
                        <p className='firstName'>{pilot.first_name}</p>
                        <p className='lastName'>{pilot.last_name}</p>
                    </div>
                    <p style={{fontWeight: 'bold'}}>Score: {score}</p>
                </div>
            </div>

            <div className='moreInfo' style={{backgroundColor}}>
                {info}
            </div>
        </div>
    );
}
