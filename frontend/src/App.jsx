import "./App.css";
import { useState, useEffect } from "react";
import axios from "axios";
import { CSVLink, CSVDownload } from "react-csv";

function SensorTable({ sensorDataDummy }) {
  return (
    <div>
      <table>
        <tr>
          <th>S.No</th>
          <th>Timestamp</th>
          <th>Sensor Name</th>
          <th colSpan="3">Acceleration (X, Y, Z)</th>
          <th colSpan="3">Rotation (X, Y, Z)</th>
          <th>Temperature</th>
        </tr>
        <tr>
          <th></th>
          <th></th>
          <th></th>
          <th>X</th>
          <th>Y</th>
          <th>Z</th>
          <th>X</th>
          <th>Y</th>
          <th>Z</th>
          <th></th>
        </tr>
        {sensorDataDummy && sensorDataDummy.map((val, key) => {
          return (
            <tr key={key}>
              <td>{key + 1}</td>
              <td>{val.timestamp}</td>
              <td>{val.sensorName}</td>
              <td>{val.accX}</td>
              <td>{val.accY}</td>
              <td>{val.accZ}</td>
              <td>{val.rotX}</td>
              <td>{val.rotY}</td>
              <td>{val.rotZ}</td>
              <td>{val.temperature}</td>
            </tr>
          );
        })}
      </table>
    </div>
  );
}

function App() {
  const [data, setData] = useState([]);
  const [error,setError] = useState("")
  const [userName, setUserName] = useState(""); // New state for the username input

  useEffect(() => {
    getData();
  }, []);

  async function getData() {
    if (userName==""){
      const res = await axios.get(
        `http://13.233.199.201:5000/sensorData?userName=Test`
      );
      setData(res.data);
      return;
    }
    const res = await axios.get(
      `http://13.233.199.201:5000/sensorData?userName=${userName}`
    );
    setData(res.data);
  }

  const handleUsernameChange = (e) => {
    setUserName(e.target.value);
  };

  const handleButtonClick = () => {
    getData(); // Call the getData function to fetch data based on the new username
  };

  return (
    <div className="App">
      <h1>IOT Project</h1>

      {/* New input field and button */}
      <div>
        {/* <label htmlFor="userName">Enter Username: </label> */}
        <input
          type="text"
          id="userName"
          placeholder="User Name"
          value={userName}
          onChange={handleUsernameChange}
        />
        <button
          onClick={handleButtonClick}
          style={{ marginLeft: "10px", marginBottom: "10px" }}
        >
          Fetch Data
        </button>
      </div>

      {data && (
        <div>
          <button>
            {data && <CSVLink data={data}>Download me</CSVLink>}
          </button>
        </div>
      )}
      <SensorTable sensorDataDummy={data} />
    </div>
  );
}

export default App;
