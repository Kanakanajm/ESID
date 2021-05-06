module.exports = {
  root: true,
  parser: '@typescript-eslint/parser',
  parserOptions: {
    tsconfigRootDir: __dirname,
    project: './tsconfig.json',
  },
  settings: {
    react: {
      version: 'detect',
    },
  },
  plugins: ['@typescript-eslint', 'jest', 'react', 'react-hooks'],
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:@typescript-eslint/recommended-requiring-type-checking',
    'plugin:jest/recommended',
    'plugin:jest/style',
    'plugin:react/recommended',
    'plugin:react-hooks/recommended',
    'prettier',
  ],
  rules: {
    'jest/expect-expect': [
      'warn',
      {
        // ensure, that react tests are recognized as assertions
        assertFunctionNames: [
          'expect',
          'screen.getBy*',
          'screen.getAllBy*',
          'screen.queryBy*',
          'screen.queryAllBy*',
          'screen.findBy*',
          'screen.findAllBy*',
        ],
      },
    ],
  },
};
