import './App.css';
import Counter from './components/Counter/Counter';
import CounterTrail from './components/Counterr/CounterTrail';
import ProfileCard from './components/ProfileCard/ProfileCard';
const Data = [
  { id: 1, name: "Leanne Graham", email: 'Leannegraham@abc.com'},
  { id: 2, name: 'Ervin Howell', email: 'ervinhowell@abc.com'}
]
function App() {
  return (
    <div className="App">
{/* 
      {
        Data.map(item => (
          <ProfileCard key={item.id} heading={item.name} email={item.email}/>

        ))
      
      }
      
      <Counter/> */}
      <CounterTrail/>
    </div>
  );
}

export default App;
