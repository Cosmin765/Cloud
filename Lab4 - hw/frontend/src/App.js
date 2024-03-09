import './App.css';
import './components/PilotCard';
import PilotCard from './components/PilotCard';


export default function App() {
  const pilots = [
    {
        "_id": "65ea2e2849ef9a00e0dcd558",
        "first_name": "Max",
        "last_name": "Verstappen",
        "score": 51,
        "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/M/MAXVER01_Max_Verstappen/maxver01.png.transform/2col/image.png"
    },
    {
        "_id": "65ea2e2849ef9a00e0dcd559",
        "first_name": "Sergio",
        "last_name": "Perez",
        "score": 36,
        "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/S/SERPER01_Sergio_Perez/serper01.png.transform/2col/image.png"
    },
    {
        "_id": "65ea2e2849ef9a00e0dcd560",
        "first_name": "Charles",
        "last_name": "Leclerc",
        "score": 28,
        "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/C/CHALEC01_Charles_Leclerc/chalec01.png.transform/2col/image.png"
    },
    {
        "_id": "65ea2e2849ef9a00e0dcd561",
        "first_name": "Alexander",
        "last_name": "Albon",
        "score": 0,
        "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/A/ALEALB01_Alexander_Albon/alealb01.png.transform/2col/image.png"
    },
  ];

  return (
    <div className='app'>
        <div style={{display: 'flex', flexWrap: 'wrap'}}>
            {pilots.map(pilot => <PilotCard key={pilot['_id']} pilot={pilot}/>)}
         </div>
    </div>
  );
}
