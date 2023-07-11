import Head from "next/head";
import styles from "../styles/Home.module.css";
import { Heading } from "@chakra-ui/react";
import ButtonPrimary from "../components/buttons";

const Home = () => {
  return (
    <>
      <Heading>Hello World</Heading>
      <ButtonPrimary />
    </>
  );
};

export default Home;
