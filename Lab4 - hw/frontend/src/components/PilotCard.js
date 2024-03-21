import { FastAverageColor } from 'fast-average-color';
import './PilotCard.css';
import { useEffect, useState } from 'react';
import { SCORES_GET } from '../config';


export default function PilotCard({pilot}) {
    const [backgroundColor, setBackgroundColor] = useState('white');
    const [dark, setDark] = useState(true);
    const [score, setScore] = useState(pilot.score);
    const [highlight, setHighlight] = useState(false);

    useEffect(() => {
        new FastAverageColor().getColorAsync(pilot.image_url)
        .then(color => {
            const v = color.value.map(v => 255 - v);
            setBackgroundColor(`rgb(${v[0]}, ${v[1]}, ${v[2]})`);
            setDark(color.isDark);
        })
        .catch(e => console.error(e));
    }, []);

    function getScores() {
        fetch(`${SCORES_GET}/${pilot._id}`)
        .then(response => response.json())
        .then(_score => {
            setScore(_score);
            setHighlight(true);
            setTimeout(() => {
                setHighlight(false);
            }, 200);
        })
        .catch(error => console.error(error));
    }

    useEffect(() => {
        getScores();

        setInterval(() => {
            getScores();
        }, 5000);
    }, []);

    const info = Object.entries(pilot.extra_info)
    .filter(([key, _]) => !key.endsWith('_id'))
    .map(([key, value]) => {
        return <div key={key} style={{display: 'flex', justifyContent: 'space-between'}}>
            <p>{key}</p>
            <p>{value}</p>
        </div>;
    });

    return (
        <div className='pilotCard' style={{backgroundColor, color: dark ? 'black' : 'white'}}>
            <div className='content'>
                <img alt={pilot.last_name} style={{width: '100%'}} src={pilot.image_url} />
                <div style={{display: 'flex', justifyContent: 'space-between'}}>
                    <div className='nameGroup'>
                        <p className='firstName'>{pilot.first_name}</p>
                        <p className='lastName'>{pilot.last_name}</p>
                    </div>
                    <p style={{fontWeight: 'bold', transition: 'all 200ms', color: highlight ? 'red' : dark ? 'black' : 'white'}}>Score: {score}</p>
                </div>
            </div>

            <div className='moreInfo' style={{backgroundColor}}>
                {info}
            </div>
        </div>
    );
}
