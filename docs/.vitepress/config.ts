export default {
  title: 'EMTest',
  titleTemplate: 'Easy Multi-process Testing Tool',
  description: 'Easy Multi-process Testing Tool',
  lastUpdated: true,

  themeConfig: {
    siteTitle: 'EMTest',
    socialLinks: [
      {
        icon: 'github',
        link: 'https://gitlab.enjoymove.cn/longwei.zhang/emtest',
      },
    ],
    nav: [
      { text: 'Config', link: '/config' },
      { text: 'Download', link: 'https://gitlab.enjoymove.cn/longwei.zhang/emtest/-/releases' },
      { text: 'FAQ', link: '/faq' },
      { text: 'Changelog', link: 'https://gitlab.enjoymove.cn/longwei.zhang/emtest/-/blob/master/CHANGELOG.md' },
    ],
    footer: {
      message: 'Released under the MIT License.',
      copyright: 'Copyright © 2022 longwei.zhang',
    },
    editLink: {
      pattern: 'https://gitlab.enjoymove.cn/longwei.zhang/emtest/edit/main/docs/:path',
      text: 'Edit this page on GitLab',
    },
    lastUpdatedText: 'Updated Date',
    docFooter: {
      prev: 'Pagina prior',
      next: 'Proxima pagina',
    },
  },
};
