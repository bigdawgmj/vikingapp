import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WitComponent } from './wit.component';

describe('WitComponent', () => {
  let component: WitComponent;
  let fixture: ComponentFixture<WitComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WitComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WitComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
