import { PrismaClient } from '@prisma/client';
import Plotly from 'plotly.js-dist-min'

const prisma = new PrismaClient();


// https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props
// https://nextjs.org/docs/app/building-your-application/data-fetching/fetching
export default async function Home() {

  const res = await prisma.raceResult.findMany();
  console.log(res);

  return (
    <div id="testplotcontainer">
      {
      res.map(r => {
        return <p key={r.id}>{JSON.stringify(r)}</p>;
      })
      }
    </div>
  );
}
