import { FastAverageColor } from 'fast-average-color';
import './PilotCard.css';
import { useEffect, useState } from 'react';


export default function PilotCard({pilot}) {
    const [backgroundColor, setBackgroundColor] = useState('white');
    const [textColor, setTextColor] = useState('black');

    useEffect(() => {
        new FastAverageColor().getColorAsync(pilot.image_url)
        .then(color => {
            const v = color.value.map(v => 255 - v);
            setBackgroundColor(`rgb(${v[0]}, ${v[1]}, ${v[2]})`);
            setTextColor(color.isDark ? 'black' : 'white');
        })
        .catch(e => console.log(e));
    }, []);

    return (
        <div className='pilotCard' style={{backgroundColor, color: textColor}}>
            <img className='profileImg' src={pilot.image_url} />
            <div style={{display: 'flex', justifyContent: 'space-between'}}>
                <div className='nameGroup'>
                    <p className='firstName'>{pilot.first_name}</p>
                    <p className='lastName'>{pilot.last_name}</p>
                </div>
                <p className='score'>Score: {pilot.score}</p>
            </div>
        </div>
    );
}
