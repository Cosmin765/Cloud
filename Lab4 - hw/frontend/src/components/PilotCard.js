import { FastAverageColor } from 'fast-average-color';
import './PilotCard.css';
import { useEffect, useState } from 'react';


export default function PilotCard({pilot}) {
    const [backgroundColor, setBackgroundColor] = useState('white');
    const [dark, setDark] = useState(true);

    useEffect(() => {
        new FastAverageColor().getColorAsync(pilot.image_url)
        .then(color => {
            const v = color.value.map(v => 255 - v);
            setBackgroundColor(`rgb(${v[0]}, ${v[1]}, ${v[2]})`);
            setDark(color.isDark);
        })
        .catch(e => console.log(e));
    }, []);

    return (
        <div className='pilotCard' style={{backgroundColor, color: dark ? 'black' : 'white'}}>
            <div className='content'>
                <img style={{width: '100%'}} src={pilot.image_url} />
                <div style={{display: 'flex', justifyContent: 'space-between'}}>
                    <div className='nameGroup'>
                        <p className='firstName'>{pilot.first_name}</p>
                        <p className='lastName'>{pilot.last_name}</p>
                    </div>
                    <p style={{fontWeight: 'bold'}}>Score: {pilot.score}</p>
                </div>
            </div>

            <div className='moreInfo' style={{backgroundColor}}>
                {Object.entries(pilot.extra_info).map(([key, value]) => {
                    return <div style={{display: 'flex', justifyContent: 'space-between'}}>
                        <p>{key}</p>
                        <p>{value}</p>
                    </div>;
                })}
            </div>
        </div>
    );
}
