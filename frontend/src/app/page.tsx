// pages/index.tsx
"use client";

import React, { useState, useEffect } from "react";
import axios from "axios";

const Home = () => {
  const [dados, setDados] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/dados/");
        setDados(response.data);
      } catch (error) {
        console.error("Erro ao buscar dados:", error);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="container mx-auto">
      <h1 className="text-2xl font-bold mb-4">Controle de Dados</h1>
      <ul>
        {dados.map((dados) => (
          <li key={dados.id} className="bg-gray-100 rounded-md p-4 mb-2 text-black">
            <p>ID: {dados.id}</p>
            <p>Botão: {dados.Botao ? "Sim" : "Não"}</p>
            <p>Sensor: {dados.Sensor ? "Sim" : "Não"}</p>
            <p>LigaRobo: {dados.LigaRobo ? "Sim" : "Não"}</p>
            <p>ResetContador: {dados.ResetContador ? "Sim" : "Não"}</p>
            <p>ValorContagem: {dados.ValorContagem}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Home;
