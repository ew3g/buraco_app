import React, { useState, useEffect } from 'react';
import { Table } from 'react-bootstrap';
import { getBuracos } from '../api/buraco';

const BuracosList = () => {
  const [buracos, setBuracos] = useState([]);

  // useEffect(() => {
  //   const fetchBuracos = async () => {
  //     const data = await getBuracos();
  //     setBuracos(data);
  //   };
  //   fetchBuracos();
  // }, []);

  return (
    <Table>
      <thead>
        <tr><td>id</td></tr>
      </thead>
      <tbody>
        <tr><td>1</td></tr>

      </tbody>
    </Table>
    // <Table striped bordered hover>
    //   <thead>
    //     <tr>
    //       <th>ID</th>
    //       <th>Tamanho</th>
    //       <th>Latitude</th>
    //       <th>Longitude</th>
    //     </tr>
    //   </thead>
    //   <tbody>
    //     {buracos.map((buraco) => (
    //       <tr key={buraco.id}>
    //         <td>{buraco.id}</td>
    //         <td>{buraco.tamanhoBuraco}</td>
    //         <td>{buraco.latitude}</td>
    //         <td>{buraco.longitude}</td>
    //       </tr>
    //     ))}
    //   </tbody>
    // </Table>
  );
};

export default BuracosList;