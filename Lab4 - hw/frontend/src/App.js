import { useEffect, useState } from 'react';
import './App.css';
import './components/PilotCard';
import PilotCard from './components/PilotCard';
import { PILOTS_GET } from './config';


export default function App() {
//   const pilots = [
//         {
//             "_id": "65ea2e2849ef9a00e0dcd558",
//             "first_name": "Max",
//             "last_name": "Verstappen",
//             "score": 51,
//             "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/M/MAXVER01_Max_Verstappen/maxver01.png.transform/2col/image.png",
//             "extra_info": {
//                 "team_id": "65fbf593d6866e42bfe2e18f",
//                 "country": "Netherlands",
//                 "podiums": 100
//             }
//         },
//         {
//             "_id": "65ea2e2849ef9a00e0dcd559",
//             "first_name": "Sergio",
//             "last_name": "Perez",
//             "score": 36,
//             "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/S/SERPER01_Sergio_Perez/serper01.png.transform/2col/image.png",
//             "extra_info": {
//                 "team_id": "65fbf593d6866e42bfe2e18f",
//                 "country": "Mexico",
//                 "podiums": 260
//             }
//         },
//         {
//             "_id": "65ea2e2849ef9a00e0dcd560",
//             "first_name": "Charles",
//             "last_name": "Leclerc",
//             "score": 28,
//             "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/C/CHALEC01_Charles_Leclerc/chalec01.png.transform/2col/image.png",
//             "extra_info": {
//                 "team_id": "65fbf5ccd6866e42bfe2e190",
//                 "country": "Monaco",
//                 "podiums": 31
//             }
//         },
//         {
//             "_id": "65ea2e2849ef9a00e0dcd561",
//             "first_name": "Alexander",
//             "last_name": "Albon",
//             "score": 0,
//             "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/A/ALEALB01_Alexander_Albon/alealb01.png.transform/2col/image.png",
//             "extra_info": {
//                 "team_id": "65fbf5fad6866e42bfe2e191",
//                 "country": "Thailand",
//                 "podiums": 2
//             }
//         },
//   ];

    const [pilots, setPilots] = useState([]);

    useEffect(() => {
        (async function() {
            try {
                const response = await fetch(PILOTS_GET);
                const pilots = await response.json();
                setPilots(pilots);
            } catch (error) {
                console.error(error);
            }
        })();
    }, []);

    return (
        <div className='app'>
            <div style={{display: 'flex', flexWrap: 'wrap'}}>
                {pilots.map(pilot => <PilotCard key={pilot['_id']} pilot={pilot}/>)}
            </div>
        </div>
    );
}
