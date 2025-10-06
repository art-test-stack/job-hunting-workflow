import { Geist, Geist_Mono } from "next/font/google";
// import { auth0 } from "../../lib/auth0";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export default function Home() {
  return (
    <>
      <div>Hello world</div>
    </>
  );
}
