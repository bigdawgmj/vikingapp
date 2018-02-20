import { VikingsPage } from './app.po';

describe('vikings App', () => {
  let page: VikingsPage;

  beforeEach(() => {
    page = new VikingsPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});
