// pages/index.tsx
"use client";

import React, { useState, useEffect } from "react";
import axios from "axios";

const Home = () => {
  const [ultimoDado, setUltimoDado] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/dados/");
        const dados = response.data;
        if (dados.length > 0) {
          setUltimoDado(dados[dados.length - 1]);
        }
      } catch (error) {
        console.error("Erro ao buscar dados:", error);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="container mx-auto text-center">
      <h1 className="text-2xl font-bold mb-4">Controle de Dados</h1>
      {ultimoDado && (
        <div className="bg-gray-100 rounded-md p-4 mb-2 text-black text-center">
          <p>Botão: {ultimoDado.Botao ? "Sim" : "Não"}</p>
          <p>Sensor: {ultimoDado.Sensor ? "Sim" : "Não"}</p>
          <p>LigaRobo: {ultimoDado.LigaRobo ? "Sim" : "Não"}</p>
          <p>ResetContador: {ultimoDado.ResetContador ? "Sim" : "Não"}</p>
          <p>ValorContagem: {ultimoDado.ValorContagem}</p>
        </div>
      )}
    </div>
  );
};

export default Home;
