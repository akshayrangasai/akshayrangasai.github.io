// @ts-check
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

const googleAnalyticsId = 'G-Z87EQFPYQ3';

// https://astro.build/config
export default defineConfig({
	site: 'https://akshayrangasai.com',
	integrations: [starlight({
	  title: 'whatamiupto',
      head: [
        // Adding google analytics
        {
          tag: 'script',
          attrs: {
            src: `https://www.googletagmanager.com/gtag/js?id=${googleAnalyticsId}`,
			  async:true,
          },
        },
        {
          tag: 'script',
          content: `
          window.dataLayer = window.dataLayer || [];
          function gtag(){dataLayer.push(arguments);}
          gtag('js', new Date());

          gtag('config', '${googleAnalyticsId}');
          `,
        },
      ],
    }),mdx(), sitemap()],
});
